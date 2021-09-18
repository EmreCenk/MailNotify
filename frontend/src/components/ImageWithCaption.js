import React from "react";

const cont = {
  backgroundColor: "#eee",
  overflow: "hidden",
  position: "relative",
  alignItems: "center"
};

const ImageWithCaption = ({ index, photo, margin, direction, top, left }) => {
  return (
    <div style={{ margin, height: photo.height, width: photo.width, ...cont }}>
      <img src={photo.src} alt="" />
      <div class="bottom-right overlay-text">{photo.caption}</div>
    </div>
  );
};

export default ImageWithCaption;
