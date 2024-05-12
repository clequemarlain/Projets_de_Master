function x = pocs_exo2(A, b, alpha, beta, T=1000,tol = 1e-6)
    [m, d] = size(A);
    n      = length(beta);
    x      = rand(d, 1);
    l      = [];
    fprintf("x_0 = %f",x);
    if d == 2 
        figure;
        plot(x(1), x(2), 'ro', 'MarkerSize', 8, 'LineWidth', 2);
        hold on;
    end
    for i = 1:T
        x_prev = x;
        for j = 1:m
            k    = m - j + 1;
            alph = alpha(k);
            ai   = A(k, :)' ;
            if (ai' * x > alph)
                x = x - max(0, ai' * x - alph) / (ai' * ai) * ai;
            end
        end
        
        for j = 1:n
            k  = n - j + 1;
            bj = b(k, :)';
            x  = bj + beta(k) / (max(norm(x - bj), beta(k))) * (x - bj);
        end
        if d == 2 
            plot(x(1), x(2), 'bo', 'MarkerSize', 8, 'LineWidth', 2);
        end
        % Check for convergence
        if norm(x - x_prev) < tol
          fprintf('Convergence en %d itérations\n', i);
            break;
        end
    end
endfunction




