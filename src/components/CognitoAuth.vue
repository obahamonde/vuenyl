<template>
<div col center>
<pre>
    {{user}}
  </pre>
  
  <Ico icon="logos:aws" @click="login" 
    icon-btn x8 sh-md r-f p-1
   title="Login with AWS Cognito"
   />
  </div>
</template>