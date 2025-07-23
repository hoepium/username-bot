function checkUsernameValidity(username) {
  if (!/^[a-zA-Z0-9_]+$/.test(username)) return "Invalid username.";
  if (username.length < 4) return "Invalid: Telegram does not allow usernames shorter than 4 characters.";
  return true;
}

function getUsernamePrice(username) {
  const lower = username.toLowerCase();

  // 4-letter Fragment-exclusive
  if (lower.length === 4 && /^[a-z]+$/.test(lower)) {
    return {
      price: "5,050 TON",
      reason: "This is a premium 4-letter username. Only available via Fragment."
    };
  }

  // Pure dictionary word example (Add your own word list as needed)
  const dictionaryWords = ['planet', 'charge', 'pillow', 'opium'];
  if (dictionaryWords.includes(lower)) {
    let price = 550;
    let extraNote = "";
    if (lower === "opium") extraNote = " (Controversial meaning limits mass appeal.)";
    return {
      price,
      reason: Short dictionary word, premium, instantly recognizable.${extraNote}
    };
  }

  // Semi-generic logic (Add/extend as needed)
  const semiGenerics = ['scopein', 'hoepium', 'dripfull', 'dementor'];
  if (semiGenerics.includes(lower)) {
    let prices = { 'scopein': 70, 'hoepium': 70, 'dripfull': 35, 'dementor': 250 };
    return {
      price: prices[lower] || 50,
      reason: "Semi-generic. Unique, but not a famous word or trend."
    };
  }

  // Random/low-market usernames
  if (/[^a-zA-Z]/.test(lower) || lower.length > 10) {
    return {
      price: 5,
      reason: "Random string, not brandable or memorable."
    };
  }

  // Default fallback
  return {
    price: 30,
    reason: "No special value detected. Modest market interest."
  };
}

module.exports = { getUsernamePrice, checkUsernameValidity };
