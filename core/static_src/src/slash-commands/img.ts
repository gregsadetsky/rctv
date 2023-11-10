import "../css/slash-img.css";

function isValidHttpUrl(string: string) {
  let url;

  try {
    url = new URL(string);
  } catch (_) {
    return false;
  }

  return url.protocol === "http:" || url.protocol === "https:";
}

let zindex = 100000;

export default function (url: string) {
  if (isValidHttpUrl(url)) {
    const img = document.createElement("img");
    img.src = url;
    img.style.position = "absolute";
    img.style.top = "0";
    img.style.left = "0";
    img.style.width = "100%";
    img.style.height = "100%";
    img.style.objectFit = "cover";
    img.style.zIndex = (zindex++).toString();
    img.style.animation = "zoominoutsinglefeatured 1s infinite";
    document.body.appendChild(img);
    setTimeout(() => {
      img.remove();
    }, 5000);
  }
}
