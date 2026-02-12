def generate_invoice(client_name, total_budget):
    """
    Calculates project financials and returns a structured invoice summary.
    Args:
        client_name (str): The name of the client.
        total_budget (float): The total project budget.
    Returns:
        str: A formatted invoice string.
    """
    # Financial Logic (Constants)
    DEPOSIT_RATE = 0.20
    TAX_RATE = 0.15

    # Calculations
    deposit = total_budget * DEPOSIT_RATE
    tax = total_budget * TAX_RATE
    total_due = deposit + tax

    # Formatting the professional output
    border = "=" * 40
    summary = (
        f"\n{border}\n"
        f"        PROJECT INVOICE: {client_name.title()}\n"
        f"{border}\n"
        f"Deposit (20%):     ${deposit:,.2f}\n"
        f"Tax Charge (15%):  ${tax:,.2f}\n"
        f"----------------------------------------\n"
        f"TOTAL INITIAL DUE: ${total_due:,.2f}\n"
        f"{border}\n"
    )
    return summary

# --- Main Execution ---
if __name__ == "__main__":
    client = input("Client's Name: ").strip()
    amount = float(input("Project Budget ($): "))

    invoice_output = generate_invoice(client, amount)
    print(invoice_output))