import "../css/slash-ticker.css";

export default function (message: string) {
  /*
    <div id="scroll-container">
      <div id="scroll-text">This is scrolling text.<div>
    </div>
  */
  // add chryon html temporarily to body with message,
  // and make it disappear after 5 seconds

  const ticker = document.createElement("div");
  ticker.id = "scroll-container";
  ticker.innerHTML = `
    <div id="scroll-text">${message}<div>
  `;
  document.body.appendChild(ticker);

  setTimeout(() => {
    document.body.removeChild(ticker);
  }, 10000);
}
