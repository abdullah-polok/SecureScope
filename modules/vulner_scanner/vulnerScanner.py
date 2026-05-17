import requests

# vulnerability Scanner Module
def check_security_headers(url):
    print(f"\nChecking security headers for: {url}\n")

    try:
        # make a request to the target URL and get the response headers
        response = requests.get(url, timeout=5)
        headers = response.headers

        #required security headers
        security_headers = {
            "X-Frame-Options": "Protects against clickjacking attacks",
            "Content-Security-Policy": "Prevents XSS and injection attacks",
            "X-Content-Type-Options": "Prevents MIME-type sniffing",
            "Strict-Transport-Security": "Enforces HTTPS connections"
        }
        
        missing = []

        # check for each required security header and print the result

        for header, description in security_headers.items():
            if header in headers:
                print(f"[OK] {header}: Present")
            else:
                print(f"[MISSING] {header}: Not found → {description}")
                missing.append(header)

        print("\n-----------------------------")
        # missing is not empty, print the number of missing headers
        if not missing:
            print("[SAFE] All important security headers are present")
        else:
            print(f"[WARNING] {len(missing)} missing security headers")

    except requests.exceptions.RequestException as e:
        print("Error connecting to target:", e)


def scan_vulnerabilities(target):
    print(f"\nScanning for vulnerabilities on: {target}")
    check_security_headers(target)


scan_vulnerabilities(input("Enter target URL: "))
