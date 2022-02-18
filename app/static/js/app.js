/* Add your Application JavaScript */
window.addEventListener('load', (event)=>{
    setInterval( ()=>{
        let fitem= document.getElementById('flash');
        if (document.contains(fitem)){
            fitem.innerHTML="";
        }
    }, 3000)
});