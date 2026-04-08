import ast
import requests
from typing import Dict, List
import bandit
import semgrep

class S4SASTEngine:
    """ deteksi vuln sebelum kompilasi"""
    
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.vulnerabilities = []
        self.patterns_db = self.load_s4_patterns()
    
    def analyze_python(self, code: str) -> Dict:
        """Analisis AST untuk deteksi backdoor, eval injection, pickle exploit"""
        tree = ast.parse(code)
        vulnerabilities = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ['eval', 'exec', 'compile']:
                        vulnerabilities.append({
                            'type': 'CODE_INJECTION',
                            'line': node.lineno,
                            'severity': 'CRITICAL',
                            's4_bypass': self.generate_bypass_method(node)
                        })
        
        return {'vulns': vulnerabilities, 's4_score': self.calculate_s4_score(code)}
    
    def generate_bypass_method(self, vulnerable_node) -> str:
        """Generate cara bypass detection (buat penetration testing)"""
        return f"# Bypass method: Use exec() with globals/locals override at line {vulnerable_node.lineno}"
