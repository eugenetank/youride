<template>
  <pre>{{ user }}</pre>
</template>

<script>
    export default {
        name: "UserProfile",
        data() {
            return {
                cars: {}
            }
        },
        created() {
            let getCars = async function () {
                let response = await fetch('http://localhost:8000/v1/cars');

                if (response.ok) {
                    this.cars = await response.json();
                } else {
                    alert("Ошибка HTTP: " + response.status);
                }

            }
        }
    }
</script>

<style scoped>

</style>
