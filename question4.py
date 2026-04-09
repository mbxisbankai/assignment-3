n=5
grand_sales=0
for n in range(1,n+1):
    sales_person=str(input("enter salesperson name:"))
    a,b,c,d,e=eval(input("enter five salesperson's sales:"))
    total_sales=a+b+c+d+e
    grand_sales+=total_sales
    print("total sales for",sales_person,":",total_sales)
print(f"grand_total:",grand_sales)    
