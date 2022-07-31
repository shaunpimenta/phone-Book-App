    
    function flashmessage(msg){
        alert(`${msg} Successfully`)
    }
    function div_show(ty)
    {
        let id;
    console.log(ty)
    if (ty==1){
        id = 'abc'
    }
    else if (ty==2) {

        id = 'abc1'
    }
    document.getElementById(id).style.display = "block";
}
    //Function to Hide Popup
    function div_hide(ty){
        let id;
    console.log(ty)
    if (ty==1){
        id = 'abc'
    }
    else if (ty==2) {
        id = 'abc1'
    }
    document.getElementById(id).style.display = "none";
}
    const sizes = ['First Name', 'Last Name', 'Mobile Number'];

    // generate the radio groups        
    const group = document.querySelector("#group");
        group.innerHTML = sizes.map((size) => `<div>
        <input type="radio" name="size" value="${size}" id="${size}">
            <label for="${size}">${size}</label>
    </div>`).join(' ');

    // add an event listener for the change event
    const radioButtons = document.querySelectorAll('input[name="size"]');
    for(const radioButton of radioButtons){
        radioButton.addEventListener('change', showSelected);
        }

    function showSelected(e) {
        console.log(e);
    if (this.checked) {
        document.querySelector('#output').innerHTML = `Please enter new ${this.value} <input type = "text" name="name1" required>
                <input class="btn" type="submit" value="submit" onclick="uptdata({{ count|length }}),flashmessage('Updated')" >`;
    console.log(this.value)
            }
        }

    function gprompt(id){
        // prompt()
        let confirmAction = confirm("Are you sure to execute this action?");
    // let confirmac=comfirm("Do you want to delete this contact");
    if (confirmAction){
        getdata(id)
            location.reload()
        }
    else{
        console.log("Cancelled")
    }
    }
    function getdata(id)
    {
        const name = document.getElementById(id).innerText
    console.log(id)

    $.ajax({
        url: '{{ url_for("deletecontact") }}',
    type: 'POST',
    data: {
        name: name
            },
    success: function (response) {
    },
    error: function (response) {
    }
        });

    };
    function uptdata(id)
    {
        const name = document.getElementById(id).innerText
    console.log(name);
    console.log(id);
    $.ajax({
        url: '{{ url_for("updatecontact") }}',
    type: 'POST',
    data: {
        name: name
            },
    success: function (response) {
    },
    error: function (response) {
    }
        });

    };
