function famosos() {
  for (let i = 1; i <= 100; i++) {
    let multiplo = (i % 3 == 0 ? "fizz":"") + (i % 5 == 0 ? "buzz":"");
    console.log(multiplo || i);
  }
}

famosos();



