function x = POCS_Inequalities(a, b, alpha, beta, x0, tol, max_iter)
    % Input:
    % a - Matrix of size (m, d) containing coefficients for inequalities
    % b - Matrix of size (n, d) containing coefficients for second type inequalities
    % alpha - Vector of size (m, 1) with threshold values for the first type inequalities
    % beta - Vector of size (n, 1) with threshold values for the second type inequalities
    % x0 - Initial guess for x (size: d x 1)
    % tol - Tolerance for convergence
    % max_iter - Maximum number of iterations
    % plot_evolution - Set to true for 2D graphical representation (only for d=2)
    
    [m, d] = size(a);
    [n, ~] = size(b);
    
    x = x0;
    
    if d == 2 
        figure;
        plot(x0(1), x0(2), 'ro', 'MarkerSize', 8, 'LineWidth', 2);
        hold on;
    end
    
    for iter = 1:max_iter
        x_prev = x;
        
        % First type inequalities
        for i = 1:m
            numerator = alpha(i) - sum(a(i, :) .* x);
            denominator = sum(a(i, :).^2);
            x = x + (numerator / denominator) * a(i, :)';
        end
        
        % Second type inequalities
        for j = 1:n
            x = min(x, b(j, :)');
        end
        
        % Check for convergence
        if norm(x - x_prev) < tol
            break;
        end
        
        if d == 2 
            plot(x(1), x(2), 'bo', 'MarkerSize', 8, 'LineWidth', 2);
        end
    end
    
    if d == 2 
        hold off;
        xlabel('x1');
        ylabel('x2');
        title('Evolution of x');
    end
end
% Example usage
 