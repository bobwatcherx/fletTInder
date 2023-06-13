from flet import *
from data import photo 


def main(page:Page):
	page.window_width=300
	page.scroll = "always"
	listlike = Row(scroll=True)
	listreject = Row(scroll=True)
	st =Stack() 


	def youchoice(e:DragUpdateEvent):
		# NOW GET PICTURE AND NAME IF YOU DRAG THE PICTURE
		getpicture = e.control.content.content.controls[0].src
		# AND GET NAME
		getname = e.control.content.content.controls[1].value

		# NOW I SET MAX AND MIN e.control.left
		e.control.left = max(-150,min(190,e.control.left + e.delta_x))
		
		# NOW YOU CAN SET MINIMUM AND MAXIMUM YOU CHOICE
		# IF LEFT DRAG THEN ADD TO listlike
		# IF YOU DRAG RIGHT AND ADD TI LIST LIKE
		# 70 is my opinion youcan change other
		if 70 <= e.control.left <=190:
			# CHANGE BGCOLOR RED
			e.control.content.bgcolor = "red"
			# IF YOU DRAG MAX TO 190 THEN WILL REMOVE 
			# AND ADD TO listreject
			if e.control.left == 190:
				st.controls.remove(e.control)
				listreject.controls.append(
					Column([
					CircleAvatar(
					foreground_image_url=getpicture
						),

						])

					)
				page.update()
		elif -57 <= e.control.left <= 70:
			e.control.content.bgcolor = "blue200"
		elif -150 <= e.control.left <= -55:
			# AND IF YOU DRAG TO LEFT ARROW 
			# THEN REMOVE AND ADD TO listlike
			e.control.content.bgcolor = "green200"
			if e.control.left == -150:
				st.controls.remove(e.control)
				listlike.controls.append(
					Column([
					CircleAvatar(
					foreground_image_url=getpicture
						),

						])

					)
				page.update()
		else:
			e.control.content.bgcolor = "blue200"
		print(e.control.left)
		print(e.control.content.content.controls[0].src)
		print(e.control.content.content.controls[1].value)
		page.update()








	# NOW ADD PHOTO AND NAME YOU MODEL TO STACK
	for x in photo:
		st.controls.append(
			# ADD GESTURE
			GestureDetector(
				mouse_cursor=MouseCursor.MOVE,
				on_pan_update=youchoice,
				left=10,
				right=10,
				top=10,
				content=Container(
					width=300,
					height=300,
					bgcolor="blue200",
					padding=10,
					content=Column([
						Image(src=x['image'],
							width=300,
							height=250,
							fit="cover"
							),
						Text(x['name'],size=25,weight="bold")
						])
					)
				)
			)



	page.overlay.append(
			Container(
				margin=margin.only(
					top=400),
				padding=10,
				content=Column([
					Text("you Like ",size=25),
				Container(
					bgcolor="green",
					padding=10,
					content=listlike
					),
				# FOR REJECT
				Text("you Like ",size=25),
				Container(
					bgcolor="red200",
					padding=10,
					content=listreject
					),
					])
				)
			)

	page.add(
		Column([
			st
			])
		)

flet.app(target=main)
