const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputs: number[] = [];

rl.on("line", (line: string) => {
  const values = line.split(" ").map(Number);
  inputs.push(...values);
}).on("close", () => {
  const N = inputs[0];
  const M = inputs[1];
  generatePermutations(N, M);
  process.exit();
});

function generatePermutations(N: number, M: number) {
  const visited: boolean[] = new Array(N + 1).fill(false);
  const permutation: number[] = [];

  function backtrack() {
    if (permutation.length === M) {
      console.log(permutation.join(" "));
      return;
    }

    for (let i = 1; i <= N; i++) {
      if (!visited[i]) {
        visited[i] = true;
        permutation.push(i);
        backtrack();
        visited[i] = false;
        permutation.pop();
      }
    }
  }

  backtrack();
}
