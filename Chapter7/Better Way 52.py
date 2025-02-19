import subprocess

result = subprocess.run(['echo', '자식 프로세스가 보내는 인사!'],
                        capture_output=True,
                        encoding='utf-8'
                        )

result.check_returncode()
print(result.stdout)
