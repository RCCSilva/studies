package tax;

import java.math.BigDecimal;

public class TestApplication {
    public static void main(String[] args) {
        // Arrange
        Budget budget = new Budget(new BigDecimal("1000"));

        // Act
        BigDecimal result = new TaxCalculator().calculate(budget, TaxType.ICMS);

        // Assert
        System.out.println(result);
    }
}
