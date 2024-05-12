%ex for convertir image
X_1 = imread('math1.jpg');  % Read the image from the file
X_1 = mean(double(X_1), 3);  % Convert the image to grayscale and store it as a matrix
[M, N] = size(X_1);  % Get the dimensions (number of rows and columns) of the matrix
%--
A = [];  % Initialize an empty matrix
K = 49;  % number of images 49
for i = 1:K
    % Read the image from a file and convert it to grayscale
    X = imread(sprintf('math%d.jpg', i));  % Replace 'filename' with your image filenames
    X = mean(double(X), 3);
    x = X(:); % Convert image to a column vector
    A = [A, x];  % put column vector x to the matrix A
end
y = imread('unknown.jpg'); % Read the image unknown 
%Y = mean(double(Y), 3); %Convert the image to grayscale and store it as a matrix
%y = Y(:); 
max_iterations = 10;
epsilon = 1e-4;  
% Implement the POCS algorithm
x_prev = double(randi([0 255],18000,1)); 
U  = A * inv(A' * A) * A';
for i = 1:max_iterations
     % Store the previous value of x
    
    x_prev   =  U* x_prev;     % Project onto C1 (Im(A))
    x_prev   = reshape(x_prev,M,N);
    x_prev(60:100,30:60) = y(60:100,30:60); %projection sur C2
    %y = imresize(y,[M N]);
    %y = reshape(y,[],1);
    x_prev = x_prev(:);
    %if norm(y - x_prev) < epsilon
    %    break;
    %end
end
%  the final result
x_prev = A * inv(A' * A) *  (A' * x_prev);
im_foun = reshape(x_prev, [M, N]);
imshow(im_foun, []);
