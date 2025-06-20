registered_fingerprints = {"fp001", "fp002", "fp003", "fp004"}
voted_fingerprints = set()

candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

def authenticate():
    print("Please scan your fingerprint (enter your fingerprint ID):")
    fp_id = input().strip()
    if fp_id in registered_fingerprints:
        if fp_id in voted_fingerprints:
            print("This fingerprint has already voted. You cannot vote again.")
            return None
        else:
            print("Fingerprint recognized. You can vote now.")
            return fp_id
    else:
        print("Fingerprint not recognized. Access denied.")
        return None

def vote(fp_id):
    print("\nCandidates:")
    for i, candidate in enumerate(candidates.keys(), 1):
        print(f"{i}. {candidate}")
    
    while True:
        choice = input("Enter the number of your chosen candidate: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(candidates):
            candidate = list(candidates.keys())[int(choice)-1]
            candidates[candidate] += 1
            voted_fingerprints.add(fp_id)
            print(f"Thank you for voting for {candidate}!")
            break
        else:
            print("Invalid choice. Please try again.")

def show_results():
    print("\nVoting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} vote(s)")

def main():
    print("Welcome to Fingerprint Voting System")
    while True:
        fp_id = authenticate()
        if fp_id:
            vote(fp_id)
        again = input("\nAnother voter? (yes/no): ").strip().lower()
        if again != "yes":
            break
    
    show_results()
    print("Voting session ended.")

if __name__ == "__main__":
    main()
