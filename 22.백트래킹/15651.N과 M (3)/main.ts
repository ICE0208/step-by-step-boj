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
  solution(N, M);
  process.exit();
});

function solution(N: number, M: number) {
  function backtrack(n: number) {
    if (n === M) {
      answer.push(arr.join(" "));
      return;
    }

    for (let i = 1; i <= N; i++) {
      arr[n] = i;
      backtrack(n + 1);
    }
  }
  const answer: string[] = [];
  const arr: number[] = [];
  backtrack(0);
  console.log(answer.join("\n"));
}
