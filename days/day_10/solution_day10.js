
const solve = () => {
  const count = {
    '{':0,
    '[':0,
    '(':0,
    '<':0
  }
  const openChars = '<([{'
  const closeChars = '>)]}'
  const stack = []

  const s = '{}{}{}{}{}{}()()(())<><><<>[][]'

  for(let i = 0; i < s.length; i += 1) {
    const selectedChar = s[i]
    
    if(openChars.includes(selectedChar)) {
      stack.push(selectedChar)
      continue
    }

    const indexOpen = openChars.indexOf(stack.pop())
    const indexClose = closeChars.indexOf(selectedChar)

    if(indexOpen !== indexClose) {
      console.log('Troll')
      break
    }

  }
}

solve()