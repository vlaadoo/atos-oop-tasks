from hashmap import Hashmap


mp = Hashmap()

if __name__ == '__main__':
    mp.put("3213", "dsdsa")
    print(mp.get("3213"))
    mp.print_hash_map()