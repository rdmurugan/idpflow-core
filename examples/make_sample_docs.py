"""Generate a small synthetic loan package for the examples (no real PII).

    python examples/make_sample_docs.py
-> writes examples/sample_docs/LN-DEMO-1/{paystub,w2,bank_statement,1003}.pdf
"""

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUT = Path(__file__).parent / "sample_docs" / "LN-DEMO-1"


def _pdf(path: Path, title: str, rows: list[tuple[str, str]]) -> None:
    p = FPDF()
    p.add_page()
    p.set_font("Helvetica", "B", 14)
    p.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    p.set_font("Helvetica", "", 11)
    for k, v in rows:
        p.set_font("Helvetica", "B", 11)
        p.cell(70, 8, k)
        p.set_font("Helvetica", "", 11)
        p.cell(0, 8, v, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    p.output(str(path))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    _pdf(OUT / "paystub.pdf", "Earnings Statement / Pay Stub",
         [("Employee:", "Jane Q. Sample"), ("Pay Frequency:", "Biweekly"),
          ("Gross Pay (this period):", "$3,250.00"), ("YTD Gross:", "$42,250.00"),
          ("Employer:", "Acme Logistics LLC")])
    _pdf(OUT / "w2.pdf", "Form W-2 Wage and Tax Statement",
         [("Employee:", "Jane Q. Sample"), ("Box 1 Wages:", "$78,000.00"),
          ("Employer EIN:", "12-3456789"), ("Tax Year:", "2025")])
    _pdf(OUT / "bank_statement.pdf", "Monthly Account Statement",
         [("Account Holder:", "Jane Q. Sample"), ("Ending Balance:", "$18,420.11")])
    _pdf(OUT / "1003.pdf", "Uniform Residential Loan Application Form 1003",
         [("Borrower:", "Jane Q. Sample"), ("Total Monthly Income:", "$6,500.00"),
          ("Loan Amount:", "$320,000.00"), ("Property Value:", "$400,000.00")])
    print(f"Wrote sample docs to {OUT}")


if __name__ == "__main__":
    main()
