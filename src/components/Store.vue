<template>
  <div class="cloud cloud1">
    <ul>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>

  <div class="cloud cloud2">
    <ul>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>

  <div class="sign font-mono">OPEN</div>
  <div class="store_roof">
    <ul>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>
  <div class="store_roof_opening"></div>
  <div class="store_window"></div>
  <div class="store_door"></div>
  <div class="store_sign">Vuenyl</div>
  <div class="store_frame_shadow"></div>
  <div class="store_frame"></div>
  <div class="store_inner_wall"></div>
  <div class="store_wall"></div>
  <div class="store_floor"></div>
  <div class="kerb">
    <div class="left"></div>
    <div class="right"></div>
  </div>
  <div class="road"></div>
  <div class="floor"></div>
</template>
<style scoped>
/* Inspired by http://dribbble.com/shots/1223440-Corner-Shop-Animation 

Only works in Google Chrome
*/
body {
  margin: 0;
  padding: 0;
  background: #a0edf7;
}

.cloud1 {
  width: 170px;
  height: 39px;
  position: absolute;
  left: 100px;
  top: 130px;
}

.cloud2 {
  width: 170px;
  height: 39px;
  position: absolute;
  left: 600px;
  top: 230px;
}

.cloud ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.cloud ul li {
  background: #fff;
  float: left;
  border-radius: 360px;
  border-right: 14px solid #f7e7eb;
  margin-left: -20px;
  opacity: 0;
  -webkit-transform: rotate(65deg);
  -webkit-animation: cloud 0.3s 1.4s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.cloud ul li:first-child {
  width: 46px;
  height: 60px;
  margin-left: 30px;
  margin-top: -20px;
}
.cloud ul li:nth-child(2) {
  width: 26px;
  height: 40px;
  margin-left: -82px;
}

.cloud ul li:nth-child(3) {
  width: 56px;
  height: 70px;
  margin-left: -20px;
  margin-top: -30px;
}

.cloud ul li:nth-child(4) {
  width: 26px;
  height: 40px;
  margin-left: -20px;
}

.floor {
  position: absolute;
  width: 0px;
  height: 0px;
  background: #868994;
  bottom: 40px;
  left: 50%;
  z-index: 5;
  -webkit-animation: floor 0.3s 0.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.road {
  position: absolute;
  width: 0px;
  height: 0px;
  background: #636272;
  bottom: 40px;
  left: 50%;
  z-index: 5;
  -webkit-animation: road 0.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.kerb {
  position: absolute;
  width: 0px;
  height: 0px;
  background: #b2b2b2;
  bottom: 45px;
  left: 50%;
  z-index: 5;
  -webkit-animation: kerb 0.3s 0.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.kerb .right {
  position: absolute;
  width: 0px;
  height: 12px;
  background: #969798;
  bottom: 0;
  right: 0;
  -webkit-animation: kerb-right 0.2s 0.4s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.kerb .left {
  position: absolute;
  width: 0;
  height: 12px;
  background: #c4d1cf;
  bottom: 0;
  left: 0;
  -webkit-animation: kerb-left 0.4s 0.6s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_floor {
  position: absolute;
  width: 0;
  height: 60px;
  background: #a24549;
  bottom: 0;
  left: 0;
  z-index: 5;
  box-shadow: 0 -5px 0 #be6151;
  -webkit-animation: store_floor 0.3s 0.7s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_wall {
  position: absolute;
  width: 0;
  height: 60px;
  background: #ffefd3;
  bottom: 0;
  left: 0;
  -webkit-animation: store_wall 0.4s 0.9s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_inner_wall {
  position: absolute;
  width: 0;
  height: 60px;
  background: #cf595d;
  bottom: 0;
  left: 0;
  z-index: 4;
  box-shadow: inset 3px 0 0 rgba(0, 0, 0, 0.1),
    inset 3px 5px 0 rgba(0, 0, 0, 0.2);
  -webkit-animation: store_inner_wall 0.4s 0.9s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_frame {
  position: absolute;
  width: 400px;
  height: 30px;
  background: #ffefd3;
  bottom: 330px;
  left: calc(50% - 150px);
  z-index: 5;
  opacity: 0;
  -webkit-animation: store_frame 0.2s 1.1s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_frame_shadow {
  position: absolute;
  width: 380px;
  height: 36px;
  background: rgba(0, 0, 0, 0.2);
  bottom: 330px;
  left: calc(50% - 140px);
  z-index: 5;
  opacity: 0;
  -webkit-animation: store_frame_shadow 0.3s 1s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_sign {
  position: absolute;
  width: 140px;
  height: 0px;
  background: #ffff8a;
  bottom: 345px;
  left: calc(50% - 30px);
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.2);
  z-index: 6;
  opacity: 0;
  -webkit-animation: store_sign 0.2s 1.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
  color: rgba(0, 0, 0, 0.4);
  font-family: Courier;
  font-size: 20px;
  text-align: center;
}

.store_door {
  position: absolute;
  width: 75px;
  height: 0px;
  background: rgb(158, 207, 215); /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* FF3.6+ */
  background: -webkit-gradient(
    linear,
    left top,
    right bottom,
    color-stop(0%, rgba(158, 207, 215, 1)),
    color-stop(6%, rgba(158, 207, 215, 1)),
    color-stop(7%, rgba(174, 219, 223, 1)),
    color-stop(10%, rgba(174, 219, 223, 1)),
    color-stop(10%, rgba(158, 207, 215, 1)),
    color-stop(22%, rgba(158, 207, 215, 1)),
    color-stop(22%, rgba(174, 219, 223, 1)),
    color-stop(33%, rgba(174, 219, 223, 1)),
    color-stop(33%, rgba(158, 207, 215, 1)),
    color-stop(40%, rgba(158, 207, 215, 1)),
    color-stop(40%, rgba(174, 219, 223, 1)),
    color-stop(42%, rgba(174, 219, 223, 1)),
    color-stop(42%, rgba(158, 207, 215, 1)),
    color-stop(76%, rgba(158, 207, 215, 1)),
    color-stop(76%, rgba(174, 219, 223, 1)),
    color-stop(87%, rgba(174, 219, 223, 1)),
    color-stop(87%, rgba(158, 207, 215, 1))
  ); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* Opera 11.10+ */
  background: -ms-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* IE10+ */
  background: linear-gradient(
    135deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#9ecfd7', endColorstr='#9ecfd7',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  border: 10px solid #fffff3;
  bottom: 57px;
  left: calc(50% + 95px);
  z-index: 6;
  opacity: 0;
  -webkit-animation: store_door 0.2s 1.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
  box-shadow: inset 2px 2px 0 rgba(0, 0, 0, 0.2);
  padding: 10px;
}

.store_door:after {
  content: "";
  position: absolute;
  top: 46%;
  left: -5px;
  width: 110px;
  height: 20px;
  background: #ffefd3;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.2);
  border-radius: 2px;
}

.store_door:before {
  content: "";
  position: absolute;
  top: 92px;
  z-index: 10;
  left: 2px;
  width: 30px;
  height: 3px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 2px;
}

.store_window {
  position: absolute;
  width: 160px;
  height: 0px;
  background: rgb(158, 207, 215); /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* FF3.6+ */
  background: -webkit-gradient(
    linear,
    left top,
    right bottom,
    color-stop(0%, rgba(158, 207, 215, 1)),
    color-stop(6%, rgba(158, 207, 215, 1)),
    color-stop(7%, rgba(174, 219, 223, 1)),
    color-stop(10%, rgba(174, 219, 223, 1)),
    color-stop(10%, rgba(158, 207, 215, 1)),
    color-stop(22%, rgba(158, 207, 215, 1)),
    color-stop(22%, rgba(174, 219, 223, 1)),
    color-stop(33%, rgba(174, 219, 223, 1)),
    color-stop(33%, rgba(158, 207, 215, 1)),
    color-stop(40%, rgba(158, 207, 215, 1)),
    color-stop(40%, rgba(174, 219, 223, 1)),
    color-stop(42%, rgba(174, 219, 223, 1)),
    color-stop(42%, rgba(158, 207, 215, 1)),
    color-stop(76%, rgba(158, 207, 215, 1)),
    color-stop(76%, rgba(174, 219, 223, 1)),
    color-stop(87%, rgba(174, 219, 223, 1)),
    color-stop(87%, rgba(158, 207, 215, 1))
  ); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* Opera 11.10+ */
  background: -ms-linear-gradient(
    -45deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* IE10+ */
  background: linear-gradient(
    135deg,
    rgba(158, 207, 215, 1) 0%,
    rgba(158, 207, 215, 1) 6%,
    rgba(174, 219, 223, 1) 7%,
    rgba(174, 219, 223, 1) 10%,
    rgba(158, 207, 215, 1) 10%,
    rgba(158, 207, 215, 1) 22%,
    rgba(174, 219, 223, 1) 22%,
    rgba(174, 219, 223, 1) 33%,
    rgba(158, 207, 215, 1) 33%,
    rgba(158, 207, 215, 1) 40%,
    rgba(174, 219, 223, 1) 40%,
    rgba(174, 219, 223, 1) 42%,
    rgba(158, 207, 215, 1) 42%,
    rgba(158, 207, 215, 1) 76%,
    rgba(174, 219, 223, 1) 76%,
    rgba(174, 219, 223, 1) 87%,
    rgba(158, 207, 215, 1) 87%
  ); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#9ecfd7', endColorstr='#9ecfd7',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  border: 3px solid #fffff3;
  bottom: 116px;
  left: calc(50% - 110px);
  z-index: 6;
  opacity: 0;
  -webkit-animation: store_window 0.2s 1.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
  box-shadow: inset 2px 2px 0 rgba(0, 0, 0, 0.2);
  padding: 10px;
}

.store_roof_opening {
  position: absolute;
  width: 216px;
  height: 9px;
  background: #ffefd3;
  bottom: 280px;
  left: calc(50% - 120px);
  z-index: 5;
  opacity: 0;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.2);
  -webkit-animation: store_roof_opening 0.2s 1.3s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_roof {
  position: absolute;
  bottom: 100px;
  left: calc(50% - 115px);
  height: 200px;
  width: 340px;
  z-index: 12;
}

.store_roof ul {
  list-style: none;
  float: left;
  margin: 0;
  padding: 0;
}

.store_roof ul li {
  width: 35px;
  height: 100px;
  opacity: 0;
  float: left;
  background: #eb6159;
  -webkit-transform: skew(-25deg) rotateX(45deg);
  -webkit-animation: store_roof 0.2s 1.5s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.store_roof ul li:nth-child(2n) {
  background: #fffbf1;
}

.store_roof ul li:nth-child(2n):after {
  background: #f7f7f7;
}

.store_roof ul li:before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  height: 10px;
  width: 100%;
  background: rgba(255, 255, 255, 0.1);
}

.store_roof ul li:after {
  content: "";
  position: absolute;
  top: 93px;
  left: 5px;
  width: 35px;
  height: 45px;
  box-shadow: 0 7px 0 rgba(0, 0, 0, 0.2);
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  background: #df5551;
  -webkit-transform: skew(18deg) rotateX(-45deg);
}

.sign {
  position: fixed;
  bottom: 180px;
  left: calc(50% + 120px);
  width: 60px;
  border-radius: 2px;
  z-index: 12;
  height: 13px;
  background: #fffff3;
  text-align: center;
  color: #99aa61;
  font-family: Arial;
  font-size: 11px;
  opacity: 0;
  -webkit-animation: sign 0.7s 1.8s linear; /* Safari 4+ */
  -webkit-animation-fill-mode: forwards;
}

.sign:after {
  content: "";
  width: 1px;
  height: 35px;
  background: #aaa;
  position: absolute;
  top: -30px;
  left: 21px;
  -webkit-transform: rotate(45deg);
}

.sign:before {
  content: "";
  width: 1px;
  height: 35px;
  background: #aaa;
  position: absolute;
  top: -30px;
  right: 21px;
  -webkit-transform: rotate(-45deg);
}

@-webkit-keyframes floor {
  0% {
    width: 0px;
    height: 0px;
  }
  100% {
    width: 100%;
    height: 40px;
    left: 0;
    bottom: 0;
  }
}

@-webkit-keyframes road {
  0% {
    width: 0px;
    height: 0px;
  }
  100% {
    width: 100%;
    height: 5px;
    left: 0;
    bottom: 40px;
  }
}

@-webkit-keyframes kerb {
  0% {
    width: 0px;
    height: 12px;
    left: 50%;
  }
  50% {
    width: 275px;
    height: 12px;
    left: 50%;
  }
  100% {
    width: 500px;
    height: 12px;
    left: calc(50% - 225px);
    bottom: 45px;
  }
}

@-webkit-keyframes kerb-right {
  0% {
    width: 0px;
  }
  100% {
    width: 90px;
    right: -40px;
  }
}

@-webkit-keyframes kerb-left {
  0% {
    width: 0px;
  }
  50% {
    width: 90px;
  }
  100% {
    width: 70px;
    left: 0px;
  }
}

@-webkit-keyframes store_floor {
  0% {
    width: 0px;
    height: 0px;
    left: 50%;
  }
  50% {
    width: 400px;
    height: 65px;
    bottom: 40px;
    left: calc(50% - 150px);
  }
  100% {
    width: 400px;
    height: 50px;
    bottom: 35px;
    left: calc(50% - 150px);
  }
}

@-webkit-keyframes store_wall {
  0% {
    width: 0px;
    height: 0px;
    left: 50%;
  }
  50% {
    width: 380px;
    height: 345px;
    bottom: 40px;
    left: calc(50% - 140px);
  }
  100% {
    width: 380px;
    height: 310px;
    bottom: 35px;
    left: calc(50% - 140px);
  }
}

@-webkit-keyframes store_inner_wall {
  0% {
    width: 0px;
    height: 0px;
    left: 50%;
  }
  50% {
    width: 360px;
    height: 300px;
    bottom: 40px;
    left: calc(50% - 130px);
  }
  100% {
    width: 360px;
    height: 280px;
    bottom: 35px;
    left: calc(50% - 130px);
  }
}

@-webkit-keyframes store_frame {
  0% {
    opacity: 0;
    bottom: 350px;
  }
  1% {
    opacity: 1;
  }
  100% {
    opacity: 1;
    bottom: 330px;
  }
}

@-webkit-keyframes store_frame_shadow {
  0% {
    opacity: 0;
    bottom: 324px;
  }
  1% {
    opacity: 0;
  }
  100% {
    opacity: 1;
    bottom: 324px;
  }
}

@-webkit-keyframes store_sign {
  0% {
    opacity: 0;
    bottom: 354px;
  }
  90% {
    opacity: 1;
  }
  100% {
    opacity: 1;
    bottom: 354px;
    height: 26px;
  }
}

@-webkit-keyframes store_door {
  0% {
    opacity: 0;
    height: 0px;
  }
  1% {
    opacity: 1;
  }
  50% {
    opacity: 1;
    height: 180px;
  }
  100% {
    opacity: 1;
    height: 160px;
  }
}

@-webkit-keyframes store_window {
  0% {
    opacity: 0;
    height: 0px;
  }
  1% {
    opacity: 1;
  }
  50% {
    opacity: 1;
    height: 160px;
  }
  100% {
    opacity: 1;
    height: 116px;
  }
}

@-webkit-keyframes store_roof_opening {
  0% {
    opacity: 0;
    height: 0px;
  }
  1% {
    opacity: 1;
  }
  50% {
    opacity: 1;
    bottom: 300px;
  }
  100% {
    opacity: 1;
    bottom: 280px;
  }
}

@-webkit-keyframes store_roof {
  0% {
    opacity: 0;
    height: 0px;
  }
  1% {
    opacity: 1;
  }
  50% {
    opacity: 1;
    height: 100px;
  }
  100% {
    opacity: 1;
    bottom: 100px;
  }
}

@-webkit-keyframes sign {
  0% {
    opacity: 0;
    bottom: 200px;
  }
  1% {
    opacity: 1;
  }
  5% {
    bottom: 180px;
  }
  30% {
    opacity: 1;
    -webkit-transform-origin: 50% -26px;
    -webkit-transform: rotate(35deg);
  }
  60% {
    opacity: 1;
    -webkit-transform-origin: 50% -26px;
    -webkit-transform: rotate(-30deg);
  }
  100% {
    opacity: 1;
    -webkit-transform-origin: 50% -26px;
    -webkit-transform: rotate(0deg);
  }
}

@-webkit-keyframes cloud {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
    -webkit-transform: scale(2) rotate(65deg);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1) rotate(65deg);
  }
}
</style>
