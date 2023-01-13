<script>
export let title = "Todo text"
export let btnTitle = "Add"

</script>
<form class="w-50 mx-auto">
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">{title}</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    </div>

    <button type="submit" class="btn btn-primary">{btnTitle}</button>
  </form>