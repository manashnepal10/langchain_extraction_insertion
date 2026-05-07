from src.chain import extraction_chain
from src.agent import agent_executor

with open("essay.txt", "r") as f:
    content = f.read()

paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
paragraphs = [p for p in paragraphs if len(p) > 100]

company_count = 0

for paragraph in paragraphs:
    result = extraction_chain.invoke({"paragraph": paragraph})
    
    for company in result.companies:
        if not company.company_name or company.company_name in ['.', 'None']:
            continue
        
        print(f"Extracted: {company.company_name}")
        
        # Agent inserts into database
        agent_executor.invoke({
            "messages": [{
                "role": "user",
                "content": (
                    f"Insert this company into the database: "
                    f"company_name={company.company_name}, "
                    f"founded_in={company.founded_in}, "
                    f"founded_by={company.founded_by}"
                )
            }]
        })
        
        print(f"-> Inserted: {company.company_name}")
        company_count += 1

print("\n****All companies processed!****")
print(f"Total Companies: {company_count}")