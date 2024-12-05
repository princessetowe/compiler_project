class RelocationTable:
    def __init__(self):
        self.entries = []  #empty list

    def add_entry(self, symbol, offset):
        self.entries.append({"symbol": symbol, "offset": offset})

    def display(self):
        print("Relocation Table:")
        print(f"{'Symbol':<15}{'Offset':<10}")
        print("-" * 25)
        for entry in self.entries:
            print(f"{entry['symbol']:<15}{entry['offset']:<10}")

    def update_offsets(self, base_address):
        for entry in self.entries:
            entry["offset"] += base_address

    def find_entry(self, symbol):
        for entry in self.entries:
            if entry["symbol"] == symbol:
                return entry
        return None
