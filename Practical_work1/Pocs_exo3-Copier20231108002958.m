function [index] = Pocs_exo3(ITER = 1000)
  A     = [];
  K     = 49; % Définissez la valeur de K en fonction de vos besoins
  m     = 150;
  n     = 120;
  for i = 1:K
      filename = sprintf('math%s.jpg', num2str(i));
      X = imread(filename);
      X = mean(double(X), 3);
      x = X(:);
      A = [A x];
  end
  y  = imread('unknown.jpg');
  x = randi([0 255],18000,1);
  B = A*inv(A'*A)*A';
  
  for iter=1:ITER
    x                = B*x;  % Project onto C1 
    x                = reshape(x,m,n);

    x(60:100, 30:60) = y(60:100, 30:60);  % Project onto C2
    
    % Display the image and include the iteration number in the title
    imshow(x, []);
    title(['Resulting Image after ', num2str(iter), ' iterations']);
    drawnow;  % Display the updated image
    if mod(iter,100)==0
      % Save the image with a unique filename
      output_filename = sprintf('result_image_iter_%d.png', iter);
      imwrite(uint8(x), output_filename);  % Convert back to uint8 if needed
    end
  
    x                = x(:);

  endfor
   

endfunction
