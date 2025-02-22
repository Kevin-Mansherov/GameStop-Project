async function editGame() {
    try{
        const confirmed = confirm("You sure you want to make this changes?");
        if(!confirmed) return;

        const game_id = document.getElementById("Game-id").value;
        const updatedGame = {
            title: document.getElementById('edit-title').value,
            creator: document.getElementById('edit-creator').value,
            year_published: document.getElementById('edit-year-published').value,
            type: document.getElementById('edit-type').value,
            price: document.getElementById('edit-price').value,
            available:document.getElementById('edit-available').value
        };


        const response = await axios.put(`http://127.0.0.1:5000/games/${game_id}`,updatedGame);
        alert(response.data.message)
        window.location.href='index.html';
    }
    catch(error){
        console.error('Error trying to edit: ', error);
        alert(error.response.data.error);
    }
}
document.addEventListener('DOMContentLoaded',()=>{
    const urlParams = new URLSearchParams(window.location.search);
    document.getElementById('Game-id').value = urlParams.get('id');document.getElementById('edit-title').value = decodeURIComponent(urlParams.get('title'));
    document.getElementById('edit-creator').value = decodeURIComponent(urlParams.get('creator'));
    document.getElementById('edit-year-published').value = urlParams.get('year');
    document.getElementById('edit-type').value = decodeURIComponent(urlParams.get('type'));
    document.getElementById('edit-price').value = urlParams.get('price');
    document.getElementById('edit-available').value = urlParams.get('available');

});