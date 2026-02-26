## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description=(
        "Perform a comprehensive analysis of the financial document to answer: {query}\n"
        "1. Use the read_data_tool to extract the full document content.\n"
        "2. Identify and extract key financial metrics: revenue, net income, EPS, margins, "
        "debt ratios, liquidity ratios, and cash flow figures.\n"
        "3. Analyze year-over-year trends where data is available.\n"
        "4. Assess the company's financial health based solely on the document data.\n"
        "5. Identify any red flags or areas of concern.\n"
        "Only use data present in the document — do not speculate or invent figures."
    ),
    expected_output=(
        "A structured financial analysis report containing:\n"
        "- Executive summary of overall financial health\n"
        "- Key financial metrics with exact figures\n"
        "- Trend analysis over reported periods\n"
        "- Strengths and areas of concern\n"
        "- Direct answer to the user's query with data citations"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description=(
        "Based on the financial document, provide investment insights for: {query}\n"
        "1. Evaluate the company's valuation indicators if available.\n"
        "2. Assess growth trajectory based on documented financial trends.\n"
        "3. Identify investment strengths and concerns backed by specific data.\n"
        "All recommendations must be grounded in the document data."
    ),
    expected_output=(
        "A structured investment analysis containing:\n"
        "- Investment thesis based on the financials\n"
        "- Valuation assessment with specific metrics\n"
        "- Growth indicators with supporting data\n"
        "- Key investment risks from the document\n"
        "Note: This is not personalized financial advice."
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description=(
        "Conduct a risk assessment based on the financial document for: {query}\n"
        "1. Assess liquidity risk using current ratio and cash flow data.\n"
        "2. Evaluate credit risk using debt-to-equity and interest coverage ratios.\n"
        "3. Identify operational risks from revenue and margin trends.\n"
        "Base all risk ratings strictly on data in the document."
    ),
    expected_output=(
        "A structured risk assessment containing:\n"
        "- Overall risk profile (Low/Medium/High) with justification\n"
        "- Liquidity, solvency and operational risk analysis\n"
        "- Risk mitigation recommendations\n"
        "- Data gaps that limit the assessment"
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

verification = Task(
    description=(
        "Verify that the uploaded document is a valid financial report.\n"
        "1. Use read_data_tool to extract the document content.\n"
        "2. Check for standard financial statements: income statement, "
        "balance sheet, and cash flow statement.\n"
        "3. Flag any missing sections or signs this is not a financial document.\n"
        "User query context: {query}"
    ),
    expected_output=(
        "A verification report containing:\n"
        "- Document type confirmation (yes/no with reasoning)\n"
        "- List of financial statements found\n"
        "- Missing or incomplete sections\n"
        "- Overall status: VERIFIED / NEEDS_REVIEW / REJECTED"
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)