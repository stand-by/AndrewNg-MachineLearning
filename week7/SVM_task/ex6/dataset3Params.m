function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

Cs = [0.01 0.03 0.1 0.3 1 3 10 30];
sigmas = [0.01 0.03 0.1 0.3 1 3 10 30];
pair = zeros(size(Cs,2)*size(sigmas,2),2);
cv_errors = zeros(size(Cs,2)*size(sigmas,2),1);

k = 0;
for i = 1:size(Cs,2),
	for j = 1:size(sigmas,2),
		k += 1;
		model = svmTrain(X, y, Cs(i), @(x1, x2) gaussianKernel(x1, x2, sigmas(j)));
		predictions = svmPredict(model, Xval);
		cv_errors(k) = mean(double(predictions ~= yval));
		pair(k,1) = Cs(i);
		pair(k,2) = sigmas(j);
	end;
end;

[v,k] = min(cv_errors);
C = pair(k,1);
sigma = pair(k,2);

% =========================================================================

end
