function [A,y] = Matrices_Im()
  A = [];
  K = 49; % Définissez la valeur de K en fonction de vos besoins

  for i = 1:K
      filename = sprintf('math%s.jpg', num2str(i));
      X = imread(filename);
      X = mean(double(X), 3);
      x = X(:);
      A = [A x];
  end
  y = imread('unknown.jpg');
  y = y(:);
endfunction
