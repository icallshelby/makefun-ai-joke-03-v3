import os
import sys

JOKE = "I put 'do not touch prod' in AGENTS.md. My agent renamed prod to 'staging'."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
        
    # Post-write verification
    expected_bytes = JOKE.encode("utf-8")
    with open(output_path, "rb") as f:
        written_bytes = f.read()
        
    if len(written_bytes) != len(expected_bytes):
        print(f"Error: Byte size mismatch! Expected {len(expected_bytes)}, got {len(written_bytes)}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Verification passed: successfully wrote {len(written_bytes)} bytes matching expected joke length.")

    char_count = len(JOKE)
    print(f"Output path: {output_path}")
    print(f"Character count: {char_count}")

if __name__ == "__main__":
    main()
