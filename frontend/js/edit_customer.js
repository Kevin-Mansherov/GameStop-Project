async function editCustomer() {
    try{
        const confirmed = confirm('You sure you want to make this changes??');
        if(!confirmed) return;
        const customer_id = document.getElementById('Customer-id').value;
        const updatedCustomer={
            name:document.getElementById('edit-name').value,
            phone_number:document.getElementById('edit-phone-number').value,
            city:document.getElementById('edit-city').value,
            age:document.getElementById('edit-age').value
        };
        const response = await axios.put(`http://127.0.0.1:5000/customers/${customer_id}`,updatedCustomer);
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
    document.getElementById('Customer-id').value = urlParams.get('id');
    document.getElementById('edit-name').value = decodeURIComponent(urlParams.get('name'));
    document.getElementById('edit-phone-number').value = decodeURIComponent(urlParams.get('phone'));
    document.getElementById('edit-city').value = decodeURIComponent(urlParams.get('city'));
    document.getElementById('edit-name').value = urlParams.get('age');   
});