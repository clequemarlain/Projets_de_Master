function x = pocs(A, b)
    [n, m] = size(A);
    x = zeros(m,1);
    T = 1000;
    err =  1e-6;
    disp(x)
    for j = 1:T

        for i = 1:n
            Ci = reshape(A(i,:), [], 1);
            x = x - (dot(Ci,x) - b(i)) / (dot(Ci,Ci)) * Ci;
            
        end
        if norm(A*x-b)<err
            break;
        end
    end
end

