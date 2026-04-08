# core/remediation.py
class S4AutoRemediation:
    """Auto fix vulnerabilities"""
    
    def fix_sql_injection(self, code: str) -> str:
        """Convert vulnerable SQL ke parameterized queries"""
        import re
        
        # Detect raw SQL concatenation
        pattern = r'cursor\.execute\(f?".*\{.*\}.*"\)'
        if re.search(pattern, code):
            # Auto fix ke parameterized
            fixed = re.sub(
                r'cursor\.execute\(f?"(.*?)".*?\)',
                r'cursor.execute("\1", params)',
                code
            )
            return f"# SQL Injection\n{fixed}"
    
    def add_security_headers(self, nginx_conf: str) -> str:
        """Add security headers otomatis"""
        headers = """
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';" always;
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
        """
        return nginx_conf + headers
