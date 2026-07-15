func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sHash := make(map[rune]int)
    tHash := make(map[rune]int)

    for _, char := range s {
        sHash[char]++
    }

    for _, char := range t {
        tHash[char]++
    }

    for char, count := range sHash {
        if tHash[char] != count {
            return false
        }
    }

    return true
}
