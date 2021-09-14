package numeral

import "testing"

type TestParameter struct {
	Arabic int
	Roman  string
}

func TestRomanNumerals(t *testing.T) {
	parameters := []TestParameter{
		{Arabic: 1, Roman: "I"},
		{Arabic: 2, Roman: "II"},
		{Arabic: 3, Roman: "III"},
		{Arabic: 4, Roman: "IV"},
		{Arabic: 5, Roman: "V"},
		{Arabic: 6, Roman: "VI"},
		{Arabic: 7, Roman: "VII"},
		{Arabic: 8, Roman: "VIII"},
		{Arabic: 9, Roman: "IX"},
		{Arabic: 10, Roman: "X"},
		{Arabic: 14, Roman: "XIV"},
		{Arabic: 18, Roman: "XVIII"},
		{Arabic: 20, Roman: "XX"},
		{Arabic: 39, Roman: "XXXIX"},
		{Arabic: 40, Roman: "XL"},
		{Arabic: 47, Roman: "XLVII"},
		{Arabic: 49, Roman: "XLIX"},
		{Arabic: 50, Roman: "L"},
		{Arabic: 100, Roman: "C"},
		{Arabic: 90, Roman: "XC"},
		{Arabic: 400, Roman: "CD"},
		{Arabic: 500, Roman: "D"},
		{Arabic: 900, Roman: "CM"},
		{Arabic: 1000, Roman: "M"},
		{Arabic: 1984, Roman: "MCMLXXXIV"},
		{Arabic: 3999, Roman: "MMMCMXCIX"},
		{Arabic: 2014, Roman: "MMXIV"},
		{Arabic: 1006, Roman: "MVI"},
		{Arabic: 798, Roman: "DCCXCVIII"},
	}
	t.Run("Convert from Arabic to Roman notation", func(t *testing.T) {

		for _, p := range parameters {
			output := ConvertToRoman(p.Arabic)

			if output != p.Roman {
				t.Errorf("got %q, want %q", output, p.Roman)
			}
		}
	})

	t.Run("Convert from Roman to Arabic notation", func(t *testing.T) {

		for _, p := range parameters {
			output := ConvertToArabic(p.Roman)

			if output != p.Arabic {
				t.Errorf("got %d, want %d", output, p.Arabic)
			}
		}
	})
}
