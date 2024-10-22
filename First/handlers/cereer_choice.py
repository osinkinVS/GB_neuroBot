available_grades = ['Стажёр', 'Опытный']

class ChoiceProfile(StatesGroup):
    doctors = State()
    grade = State()

@router.message(Command("prof"))
async def cmd_prof(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите нужное направление",
        reply_markup=make_row_keyboard(available_doctors)
    )
    await state.set_state(ChoiceProfile.doctors)

@router.message(ChoiceProfile.doctors, F.text.in_(available_doctors))
async def doctors_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        text="Выберите квалификацию",
        reply_markup=make_row_keyboard(available_grades)
    )
    await state.set_state(ChoiceProfile.grade)

@router.message(ChoiceProfile.doctors)
async def doctors_chosen(message: types.Message):
    await message.answer(
        text="Выберите направление",
        reply_markup=make_row_keyboard(available_doctors)
    )
