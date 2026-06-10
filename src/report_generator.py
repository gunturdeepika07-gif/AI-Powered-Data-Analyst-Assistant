def generate_report(
        selected_column,
        insights,
        summary,
        ai_response
):
    report = f"""
AI POWERED DATA ANALYST REPORT
============================================

Selected Column:
{selected_column}

INSIGHTS
--------------------------------------
"""

    for insight in insights:
        report += f"-{insight}\n"

    report += f"""
SUMMARY
-------------------------------
{summary}
AI ANALYSIS
-------------------------------

{ai_response}
"""
    return report