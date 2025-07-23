function roastUsername(username) {
  const templates = [
    So your username is @${username}? Looks like you picked it out of a bargain bin and thought no one would notice.,
    @${username} — nothing says 'I tried too hard' like forcing swag into five letters.,
    @${username}: If you were any more unoriginal, you’d be used as a CAPTCHA.,
    @${username} spent more time thinking of this name than anyone ever will talking to them.,
    @${username} is the type of name that makes people glad Telegram has mute.
  ];
  // Pick one at random
  return templates[Math.floor(Math.random() * templates.length)];
}

module.exports = { roastUsername };
