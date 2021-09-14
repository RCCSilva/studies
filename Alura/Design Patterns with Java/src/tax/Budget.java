package tax;

import java.math.BigDecimal;

public class Budget {
    private BigDecimal value;

    public Budget(BigDecimal value) {
        this.value = value;
    }

    public BigDecimal getValue() {
        return this.value;
    }
}
