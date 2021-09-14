package tax;

import java.math.BigDecimal;

public class TaxCalculator {
    public BigDecimal calculate(Budget budget, TaxType taxType) {
        return switch (taxType) {
            case ICMS -> budget.getValue().multiply(new BigDecimal("0.1"));
            case ISS -> budget.getValue().multiply(new BigDecimal("0.06"));
        };
    }
}
