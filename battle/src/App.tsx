import     { useState } from "react";
import { styled } from "@mui/system";
import slime from "./assets/slime.png";

interface AnimatedImageProps {
  animated: boolean;
}

const Container = styled("div")({
  background: "black",
  height: "100vh",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
});

const AnimatedImage = styled("img")<AnimatedImageProps>(({ animated }) => ({
  transform: `scaleX(${animated ? -1 : 1})`,
  transition: "transform 1s",
}));

function App() {
  const [animated, setAnimated] = useState(false);

  const handleButtonClick = () => {
    setAnimated(!animated);
  };

  return (
    <Container>
      <AnimatedImage src={slime} width={"200"} height={"200"} animated={animated} />
      <AnimatedImage src={slime} width={"200"} height={"200"} animated={!animated} />
      <button onClick={handleButtonClick}>ボタン</button>
    </Container>
  );
}

export default App;
