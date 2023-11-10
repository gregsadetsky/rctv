import "../css/slash-chyron.css";

export default function (message: string) {
  /*
    <div id="scroll-container">
      <div id="scroll-text">This is scrolling text.<div>
    </div>
  */
  // add chryon html temporarily to body with message,
  // and make it disappear after 5 seconds

  const chyron = document.createElement("div");
  chyron.id = "scroll-container";
  chyron.innerHTML = `
    <div id="scroll-text">${message}<div>
  `;
  document.body.appendChild(chyron);

  // setTimeout(() => {
  //   document.body.removeChild(chyron);
  // }, 5000);
}
