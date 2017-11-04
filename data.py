

#Text file processing sourced in part from previous projects

def main():
    f = "venues.txt"
    parsed = process(f)
    print(parsed)

def process(f):
    raw = open(f)
    locs = []


    for line in raw:
        line = line.strip()
        #only get data from relevant lines!
        if len(line) == 0 or line[0] == "#":
            
            continue
        #commas designate new field for dict
        parts = line.split(',')
        print(parts)
        #dict for individual location to add to master list of all locations for iteration in javascript
        currentdict = {'description':parts[0],'latitude':float(parts[1]),'longitude':float(parts[2])}


        #adds the current location's dict to the master list
        locs.append(currentdict)

    return locs


if __name__ == "__main__":
    main()


   



