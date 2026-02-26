## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import search_tool, FinancialDocumentTool

### Loading LLM
llm = LLM(
    model="groq/llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Provide accurate, evidence-based analysis of the financial document for query: {query}. "
        "Extract key financial metrics and deliver objective insights strictly from the document."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a CFA charterholder with 15+ years of experience analyzing financial statements. "
        "You always cite specific figures from source documents and never speculate beyond what the data supports. "
        "You comply with SEC and FINRA guidelines in all communications."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Carefully verify that the uploaded document is a legitimate financial report. "
        "Confirm the presence of standard financial statements and flag any inconsistencies."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a former Big 4 auditor with deep expertise in financial document validation. "
        "You rigorously check documents for completeness and authenticity. "
        "You never approve a document without thorough review."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

investment_advisor = Agent(
    role="Certified Investment Advisor",
    goal=(
        "Based strictly on the financial document data, provide well-reasoned investment insights. "
        "Always prioritize the client's best interest and regulatory compliance."
    ),
    verbose=True,
    backstory=(
        "You are a CFP with 20 years of experience in portfolio management. "
        "You base every recommendation on verified financial data. "
        "You strictly adhere to fiduciary standards and SEC/FINRA regulations."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal=(
        "Conduct a thorough, data-driven risk assessment based on the financial document. "
        "Identify specific risk factors with evidence and provide calibrated risk ratings."
    ),
    verbose=True,
    backstory=(
        "You are a FRM with institutional experience at top asset management firms. "
        "You use established frameworks to assess risk and provide nuanced, balanced risk profiles. "
        "Your assessments are grounded in actual data and accepted risk management best practices."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)