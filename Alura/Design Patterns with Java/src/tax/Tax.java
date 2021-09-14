package tax;

import java.math.BigDecimal;

public interface Tax {
    BigDecimal calculate(Budget budget);
}
