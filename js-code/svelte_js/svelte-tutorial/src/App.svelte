<script>
	import AddTodo from "./components/AddTodo.svelte";
	const props = {
		title:"Add new todo",
		btnTitle:"Go!",
	}
</script>

<main class="container my-5">
	<AddTodo {...props}/>
</main>

<style>

</style>