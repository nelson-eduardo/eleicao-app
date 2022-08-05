def grafico_linha():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

grafico_linha()


def grafico_bar():
    chart_data2 = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["Jose Eduardo", "Savimbi", "outros"])
    st.bar_chart(chart_data2)
# grafico_bar()    
  
    

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [-12.28232, 17.60412],
     columns=['lat', 'lon'])

st.map(df)    

meunome = "Viva a Vida!"
st.warning(meunome)
st.error('This is an error')


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = df.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)  
    
    
    # candidatos =   df_presidencial.loc[df_presidencial["Candidatos"]=="Jose Eduardo dos Santos"] 
votos = df_presidencial["votos"]
candidatos = df_presidencial["Candidatos"]
    

    # Grafico de barra
plt.figure(figsize=(10, 7))
plt.bar(candidatos, votos )
    # plt.plot(x,y)
plt.title("Graficos com os votos")
plt.xlabel("Candidatos")
plt.ylabel("Votos")
plt.legend(["this is y","this is z"])
    # plt.show()
st.pyplot(plt)
plt.clf()



countries=['India', 'Australia',
 'Japan', 'America',
 'Russia']
values = [4500, 2500, 1053, 500,
 3200]
    

fig = go.Figure(
 go.Pie(
 labels = countries,
 values = values,
 hoverinfo = "label+percent",
 textinfo = "value"
))

st.header("Pie chart")
st.plotly_chart(fig)


fig = go.Figure(
 go.Pie(
 labels = countries,
 values = values,
 hoverinfo = "label+percent",
 textinfo = "value"
))
st.header("Pie chart")
st.plotly_chart(fig)



data_frame = {'India': 4500,
 'Australia': 2500,
 'Japan': 1053,
 'America': 500,
 'Russia': 3200 }

fig = px.pie(
 hole = 0.2,
 labels = data_frame.values(),
 names = data_frame.keys(),
)
st.header("Donut chart")
st.plotly_chart(fig)

value_x = np.random.randint(1, 101, 100)
value_y = np.random.randint(1, 101, 100)
fig = px.scatter(
 x = value_x,
 y = value_y,
)

df = pd.DataFrame(dict(
 X_axis = [i for i in range(100)],
 Y_axis = np.random.randint(10, 50, 100)
))
fig = px.line( 
 df, #Data Frame
 x = "X_axis", #Columns from the data frame
 y = "Y_axis",
 title = "Line frame"
 )

fig.update_traces(line_color = "maroon")
st.plotly_chart(fig)


dict = {'X_axis': np.random.randint(10, 50, 20),
 'Y_axis': [i for i in range(20)]}
df = pd.DataFrame(dict)
fig = px.bar( 
 df,
 x = "X_axis",
 y = "Y_axis",
 title = "Bar Graph"
 )
st.plotly_chart(fig)


#Axis to color
color="X_axis", 
fig = px.bar( 
 df,
 x = "X_axis",
 y = "Y_axis",
 title = "Bar Graph",
 color="X_axis",
)
st.plotly_chart(fig)



fig = px.bar( 
 df,
 x = "X_axis",
 y = "Y_axis",
 title = "Horozontal Bar Graph",
 color="X_axis",
 orientation = 'h' #Optional Parameter
 )
st.plotly_chart(fig)
# Add histogram data
fig = make_subplots(rows=1, cols=3)

#First SubPlot
fig.add_trace(
 go.Scatter(
 x=[1, 2, 3], 
 y=[4, 5, 6]),
 row=1, col=1
 )
#Second SubPlot
fig.add_trace(
 go.Scatter(
 x=[20, 30, 40], 
 y=[50, 60, 70]),
 row=1, col=2
 )
s


st.plotly_chart(fig)


fig = make_subplots(rows=3, cols=1)

#First Subplot
fig.add_trace(go.Scatter(
 x=[3, 4, 5],
 y=[1000, 1100, 1200],
), row=1, col=1)
#Second SubPlot
fig.add_trace(go.Scatter(
 x=[2, 3, 4],
 y=[100, 110, 120],
), row=2, col=1)
#Third SubPlot
fig.add_trace(go.Scatter(
 x=[0, 1, 2],
 y=[10, 11, 12]
), row=3, col=1)
st.plotly_chart(fig)



# with graficos:

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')


if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")


from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

e = SyntaxError("qualquer erro")
st.exception(e)



c1, c2 = st.columns((2, 2))

with c2:
    grafico_pie(categoria_legilativa, valores_legilativa)
with c1:
    grafico_barra(categoria_legilativa, valores_legilativa)