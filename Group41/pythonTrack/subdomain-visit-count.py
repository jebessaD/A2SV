class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store={}
        for domain in cpdomains:
            num,dom=domain.split(" ")
            subdomain=dom.split(".")
            visit=""
            for d in reversed(subdomain):
                visit = d + visit
                if visit in store:
                    store[visit]+=int(num)
                else:
                    store[visit]=int(num)
                visit = "."+visit
                
        ans=[]
        for web in store:
            ans.append(str(store[web])+ " " + web)
        return ans